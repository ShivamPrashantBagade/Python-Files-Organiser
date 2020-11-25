import os
import shutil

FolderName = ["Videos", "Documents", "Setupfiles", "Images", "Other"]


def CreateFolderIfNotExist(FolderName):

    for i in FolderName:
        if not os.path.exists(i):
            os.mkdir(i)


CreateFolderIfNotExist(FolderName)

AllFiles = os.listdir()

imageExtensions = [".png", '.jpeg', '.jpg']
videosExtensions = [".mp4"]
documentsExtensions = [".pdf", ".docx", ".html", ".txt"]
setupfilesExtension = [".exe", ".iso", ".jar", ".xlsm", ".zip"]

for i in FolderName:
    if i in AllFiles:
        AllFiles.remove(i)
    else:
        pass

def Copy(FileExtension, Destination):

    for f in AllFiles:

        for e in FileExtension:

            if e in f:
                shutil.move(os.path.join(f), os.path.join(Destination, f))


Copy(imageExtensions, "Images")
Copy(videosExtensions, "Videos")
Copy(setupfilesExtension, "Setupfiles")
Copy(documentsExtensions, "Documents")

for f in AllFiles:

	shutil.move(os.path.join(f), os.path.join("Other", f))


print("FIles moved successfully")
