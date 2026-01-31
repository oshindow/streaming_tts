This repository contains several test scripts for running xcodec2 and llasa with different settings and transformer versions.

`test_xcodec2.py` reconstructs speech directly from a waveform input.

`test_xcodec2_load.py` synthesizes speech from previously saved codec files.

`test_llasa_attn_sink.py` is the attention sink version of llasa, compatible with transformers==4.34.0.

`test_llasa.py` is the original llasa version, compatible with transformers==4.45.2.

To run xcodec2, first install the required packages:
```
pip install xcodec2==0.1.5
pip install transformers==4.45.2
```
Then run:
```
python3 test_xcodec2.py
```

To run llasa:
```
./run.sh
```
Make sure the transformer version matches the script you are running.