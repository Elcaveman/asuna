from .models import Disease

if __name__ == '__main__':
    Disease.compile_disease()
    print("Done :Diseases compilation into a .json file")
    Disease.compile_intents()
    print("Done :Intents compilation into a .json file")