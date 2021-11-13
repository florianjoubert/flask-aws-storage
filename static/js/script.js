const fileSelector = document.getElementById('inputFile');
const btnShowAll = document.getElementById('showAll');
const btnShowLimit = document.getElementById('showLimit');
const listFull = document.getElementById('listFull');
const listLimit = document.getElementById('listLimit');

var divFile = document.getElementById("fileToUpload");
var inputBloc = document.getElementById("inputBlock");
var fileName = document.getElementById("fileName");
var fileSize = document.getElementById("fileSize");
var fileImage = document.getElementById("fileImage");

if(fileSelector){
  fileSelector.addEventListener('change', (event) => {
    const fileList = event.target.files;
    if (fileList.length == 0) {
      divFile.classList.add("hidden");
      inputBloc.classList.remove("hidden");
      fileName.innerHTML = "";
      console.log("fichier supprimé");
    } else {
      var size;
      if(fileList[0].size > 1000000){
        size = (fileList[0].size / 1000000).toFixed(1) + " MB";
      }
      else{
        size = (fileList[0].size / 1000).toFixed(1) + " KB";
      }
      if(fileList[0].name.includes(".jpeg") || fileList[0].name.includes(".jpg") || fileList[0].name.includes(".png") || fileList[0].name.includes(".webp") || fileList[0].name.includes(".svg") || fileList[0].name.includes(".gif")){
        fileImage.src="./static/img/icons/Image.png";
      }
      else if(fileList[0].name.includes(".pdf")){
        fileImage.src="./static/img/icons/Page.png";
      }
      else if (fileList[0].name.includes(".zip") || fileList[0].name.includes(".rar") || fileList[0].name.includes(".7z") || fileList[0].name.includes(".gz") || fileList[0].name.includes(".bz2")){
        fileImage.src="./static/img/icons/Folder.png";
      }
      else{
        fileImage.src="./static/img/icons/Document.png";
      }
      fileSize.innerHTML =size;
      fileName.innerHTML = fileList[0].name;
      divFile.classList.remove("hidden");
      inputBloc.classList.add("hidden");
      for (var i = 0; i < fileList.length; i++) {
        console.log(fileList[i]);
      }
    }
  });
}


function deleteFile(){
  document.getElementById("inputFile").value = "";
  divFile.classList.add("hidden");
    inputBloc.classList.remove("hidden");
    fileName.innerHTML = "";
    console.log("fichier supprimé");
}
//document.getElementById("uploadCaptureInputFile").value = "";

function showAllUploads(){
  listFull.classList.remove("hidden");
  listLimit.classList.add("hidden");
  btnShowAll.classList.add("hidden");
  btnShowLimit.classList.remove("hidden");

}
function showLimitUploads(){
  listFull.classList.add("hidden");
  listLimit.classList.remove("hidden");
  btnShowAll.classList.remove("hidden");
  btnShowLimit.classList.add("hidden");

}
var copyUrl = document.getElementById("copyUrl");
var notifPanel = document.getElementById("notifPanel");
var endpoint = "https://wojo.s3.naitways.net/preprod/"

function copyClip(text){
  navigator.clipboard.writeText(endpoint + text);
  notifPanel.classList.add("transform");
  notifPanel.classList.add("ease-out");
  notifPanel.classList.add("duration-300");
  notifPanel.classList.add("opacity-100");
  notifPanel.classList.remove("ease-in");
  notifPanel.classList.remove("duration-100");
  notifPanel.classList.remove("opacity-0");

  notifPanel.classList.remove("translate-y-2");
  notifPanel.classList.remove("opacity-0");
  notifPanel.classList.remove("sm:translate-y-0");
  notifPanel.classList.remove("sm:translate-x-2");
  
  notifPanel.classList.add("translate-y-0");
  notifPanel.classList.add("opacity-100");
  notifPanel.classList.add("sm:translate-x-0");
  setTimeout(function() {
    removeToast();
  }, 3000);
}

function removeToast(){
  notifPanel.classList.add("translate-y-2");
  notifPanel.classList.add("sm:translate-y-0");
  notifPanel.classList.add("sm:translate-x-2");

  notifPanel.classList.remove("transform");
  notifPanel.classList.remove("ease-out");
  notifPanel.classList.remove("duration-300");
  notifPanel.classList.remove("opacity-100");
  notifPanel.classList.add("ease-in");
  notifPanel.classList.add("duration-100");
  notifPanel.classList.add("opacity-0");
}