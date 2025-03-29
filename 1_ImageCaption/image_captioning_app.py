import gradio as gr
import torch
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration
import os # Needed for examples if using local files

# --- Configuration ---
MODEL_NAME = "Salesforce/blip-image-captioning-base"
# Define example image paths (replace with your actual image paths)
# Ensure these images exist or remove/comment out the 'examples' list
EXAMPLE_IMAGES = [
    'cat.jpg'
]
# Filter out non-existent example files to prevent errors
EXAMPLE_IMAGES = [img for img in EXAMPLE_IMAGES if os.path.exists(img)]

# --- Device Setup ---
# Check if CUDA (GPU support) is available, otherwise use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# --- Load Model and Processor ---
try:
    # Load the pretrained processor and model
    # Load onto the determined device (GPU or CPU)
    processor = AutoProcessor.from_pretrained(MODEL_NAME)
    model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME).to(device)
    print("Model and processor loaded successfully.")
except Exception as e:
    print(f"Error loading model or processor: {e}")
    # Optionally, exit or handle the error gracefully
    exit()

# --- Captioning Function ---
def caption_image(input_image: Image.Image):
    """
    Generates a caption for the input PIL Image.
    """
    # Ensure the input is a PIL Image (Gradio handles this with type="pil")
    if not isinstance(input_image, Image.Image):
        raise TypeError("Input must be a PIL Image.")

    # Convert image to RGB if it's not already (some models require RGB)
    raw_image = input_image.convert('RGB')

    try:
        # Process the image: prepare it for the model
        # Move inputs to the same device as the model
        inputs = processor(images=raw_image, return_tensors="pt").to(device)

        # Generate a caption for the image
        # Adjust max_length or other generation parameters if needed
        with torch.no_grad(): # Disable gradient calculation for inference
             out = model.generate(**inputs, max_length=50)

        # Decode the generated tokens (IDs) back into text
        # skip_special_tokens=True removes tokens like [CLS], [SEP], etc.
        caption = processor.decode(out[0], skip_special_tokens=True)

        return caption

    except Exception as e:
        print(f"Error during caption generation: {e}")
        return "Sorry, an error occurred during caption generation."

# --- Gradio Interface ---
# Use gr.Blocks for more layout control if needed in the future
iface = gr.Interface(
    fn=caption_image,
    # Input: Use gr.Image, specify type="pil" to receive PIL Image directly
    inputs=gr.Image(type="pil", label="Upload Image"),
    # Output: Use gr.Textbox for more control (like adding a label)
    outputs=gr.Textbox(label="Generated Caption"),
    title="Image Captioning with BLIP",
    description="Upload an image and this app will generate a caption using the Salesforce BLIP model. Runs on GPU if available.",
    # Add examples (list of file paths or URLs)
    examples=EXAMPLE_IMAGES if EXAMPLE_IMAGES else None,
    # Add a theme for better aesthetics (optional)
    theme=gr.themes.Soft(),
    allow_flagging="never" # Optional: disable flagging
)

# --- Launch the App ---
if __name__ == "__main__":
    # share=False keeps it local, set share=True to create a temporary public link
    iface.launch(share=False)