import argparse
import re
import subprocess

def get_audio_devices():
    cmd = "powershell Get-AudioDevice -list"
    output = subprocess.check_output(cmd, shell=True, text=True)
    devices = re.findall(r'Index\s+:\s+(\d+)\s+.*?Name\s+:\s+(.*?)\s+ID\s+:\s+{(.*?)}', output, re.DOTALL)
    return devices

def set_audio_device(device_name, devices):
    device_words = device_name.lower().split()
    
    for index, name, _ in devices:
        lower_name = name.lower()
        
        if all(word in lower_name for word in device_words):
            cmd = f"powershell set-audiodevice -index {index}"
            subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def switch_audio(audio_output):
    devices = get_audio_devices()
    set_audio_device(audio_output, devices)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Switch audio output device")
    parser.add_argument("-o", "--output", type=str, help="Specify the audio output device name")
    args = parser.parse_args()
    
    if args.output:
        switch_audio(args.output)
    else:
        print("Please specify the audio output device using -o or --output argument.")
