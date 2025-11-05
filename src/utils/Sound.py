path = "assets/sounds" # Path to sound folder

def GetSoundById(soundId: str):
    selected_sound = None # Variable for saving the sounds path, which we'll return if it exists
    try:
        selected_sound = f"{path}/{soundId.lower()}.mp3"
    except:  # noqa: E722
        raise ImportError(f"No sound named {soundId.lower()}") # Error output if the sound wasn't found
    
    return selected_sound