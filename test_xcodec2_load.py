import torch
import soundfile as sf


from xcodec2.modeling_xcodec2 import XCodec2Model
 
model_path = "HKUSTAudio/xcodec2"  
 
model = XCodec2Model.from_pretrained(model_path)
model.eval().cuda()   

 
with torch.no_grad():
 
    vq_code = torch.load("speech_tokens.pt").cuda()  # Shape: (1, T)
    print("Code:", vq_code )  
    
    recon_wav = model.decode_code(vq_code).cpu()       # Shape: (1, 1, T')

 
sf.write("gen_zh_reconstructed.wav", recon_wav[0, 0, :].numpy(), 16000)
print("Done! Check reconstructed.wav")
