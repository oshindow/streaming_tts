# To run llasa (original version):
# 
# CUDA_VISIBLE_DEVICES=1 python3 test_llasa.py
# python3 test_xcodec2_load.py 
 

# To run llasa with attention sink:
#
CUDA_VISIBLE_DEVICES=1 python3 test_llasa_attn_sink.py 
python3 test_xcodec2_load.py 