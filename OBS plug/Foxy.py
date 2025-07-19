import random
import time
try:
    import obsws_python as obs
    print("obsws_python imported successfully!")
except ImportError as e:
    print(f"Import error: {e}")
    exit()

try:
    cl = obs.ReqClient(host='localhost', port=4455)
    print("Connected successfully!")
    
    # List available scenes
    scenes = cl.get_scene_list()
    print("Available scenes:")
    for scene in scenes.scenes:
        print(f"  - {scene['sceneName']}")

    def jumpscare(cl):
        print("lol")
        try:
            cl.set_current_program_scene("Foxy Jumpscare")
            time.sleep(3)
            cl.set_current_program_scene("Scene")
        except Exception as e:
            print("uh oh, bug")

    def main(cl): 
        print("Running")      
        try:
            while True:
                waitTime = random.randint(600, 900)
                time.sleep(waitTime)
                jumpscare(cl)
        except KeyboardInterrupt:
            print("ending")
    
    main(cl)
    cl.disconnect()        
   
except Exception as e:
    print(f"Connection failed: {e}")