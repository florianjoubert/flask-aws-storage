function switchToggle() {
  var btn = document.getElementById("toggleButton");
  var spn = document.getElementById("toggleSpan");
  var spnUpload = document.getElementById("spnUpload");
  if (btn.classList.contains("bg-blue-600")) {
    btn.classList.remove("bg-blue-600");
    btn.classList.add("bg-gray-200");
    spn.classList.remove("translate-x-5");
    spn.classList.add("translate-x-0");
    spnUpload.innerHTML = 'Test environment'
  } else {
    btn.classList.add("bg-blue-600");
    btn.classList.remove("bg-gray-200");
    spn.classList.add("translate-x-5");
    spn.classList.remove("translate-x-0");
    spnUpload.innerHTML = 'Upload in production'
  }

}

function toggleUpload() {
  var upload = document.getElementById("toggleUpload");
  var recent = document.getElementById("toggleRecent");
  upload.setAttribute("class", "w-32 ease-in-out duration-200 relative bg-blue-600 py-2 px-6 border-blue-700 rounded-full shadow-sm text-sm font-medium text-white whitespace-nowrap  focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-blue-700 focus:ring-white focus:z-10");
  recent.setAttribute("class", "w-32 ease-in-out duration-200 rml-0.5 relative py-2 px-6 border border-transparent rounded-full text-sm font-medium  whitespace-nowrap  focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-blue-700 focus:ring-white focus:z-10");

}

function toggleRecent() {
  var upload = document.getElementById("toggleUpload");
  var recent = document.getElementById("toggleRecent");
  recent.setAttribute("class", "w-32  ease-in-out duration-200 elative bg-blue-600 py-2 px-6 border-blue-700 rounded-full shadow-sm text-sm font-medium text-white whitespace-nowrap  focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-blue-700 focus:ring-white focus:z-10");
  upload.setAttribute("class", "w-32  ease-in-out duration-200 rml-0.5 relative py-2 px-6 border border-transparent rounded-full text-sm font-medium  whitespace-nowrap  focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-blue-700 focus:ring-white focus:z-10");

}
const fileSelector = document.getElementById('inputFile');
var divFile = document.getElementById("fileToUpload");
var inputBloc = document.getElementById("inputBlock");
var fileName = document.getElementById("fileName");
fileSelector.addEventListener('change', (event) => {
  const fileList = event.target.files;
  if (fileList.length == 0) {
    divFile.classList.add("hidden");
    inputBloc.classList.remove("hidden");
    fileName.innerHTML = "";
    console.log("fichier supprimé");
  } else {
    fileName.innerHTML = fileList[0].name;
    divFile.classList.remove("hidden");
    inputBloc.classList.add("hidden");
    for (var i = 0; i < fileList.length; i++) {
      console.log(fileList[i]);
    }
  }
});

function deleteFile(){
  document.getElementById("inputFile").value = "";
  divFile.classList.add("hidden");
    inputBloc.classList.remove("hidden");
    fileName.innerHTML = "";
    console.log("fichier supprimé");
}
//document.getElementById("uploadCaptureInputFile").value = "";