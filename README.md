# RNABricks-Dataset-Downloader
An open-source downloader for the RNABricks dataset for RNA 3D structure

While large amounts of research has been done to predict the 3D structure of proteins (such as Google's AlphaFold), not much research has been done to predict the 3D structure of RNA, due to lack of data, as well as the overwhelming complexity of RNA. Additionally, no open-source downloaders existed for the RNABricks dataset prior to this one, which will hopefully allow scientists and other researchers to more easily develop models to simulate the folding of RNA.

# Running the Downloader

Running the downloader only requires the json library (as far as external python libraries go), and can be run in the command prompt or terminal. All zip files will be stored in the "RNABricks Data" folder.

```
python ./RNABricks-Dataset-Downloader/download_data.py
```

All of the specific RNA IDs are also in this repository for reference.
