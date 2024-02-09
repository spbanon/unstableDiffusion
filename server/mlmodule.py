import torch 
from diffusers import StableDiffusionPipeline


class MlModule:
    def __init__(self) -> None:
        self.model_id = "runwayml/stable-diffusion-v1-5"
        self.pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float32)
        self.image = None
        
    def __call__(self, prompt: str):
        self.image = self.pipe(prompt).images[0]
        return self.image