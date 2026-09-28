import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


class LocalQwenAdapter:
    """
    Controlled local adapter for Qwen3-0.6B.

    This adapter does not perform scientific validation,
    evidence retrieval, decision making, or human approval.
    Those controls remain outside the model adapter.
    """

    def __init__(self, model_path):
        self.model_path = model_path
        self.device = "cpu"

        if torch.cuda.is_available():
            raise RuntimeError(
                "GPU execution is not permitted by this adapter."
            )

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            local_files_only=True
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            local_files_only=True,
            torch_dtype=torch.float32
        )

        self.model.to(self.device)
        self.model.eval()

    def generate(
        self,
        prompt,
        max_new_tokens=32,
        do_sample=False
    ):
        if not isinstance(prompt, str):
            raise TypeError("Prompt must be a string.")

        if not prompt.strip():
            raise ValueError("Prompt must not be empty.")

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt"
        )

        inputs = {
            key: value.to(self.device)
            for key, value in inputs.items()
        }

        with torch.no_grad():
            output_ids = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=do_sample,
                pad_token_id=self.tokenizer.eos_token_id
            )

        generated_ids = output_ids[
            0,
            inputs["input_ids"].shape[1]:
        ]

        return self.tokenizer.decode(
            generated_ids,
            skip_special_tokens=True
        )
