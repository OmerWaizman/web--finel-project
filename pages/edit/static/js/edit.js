var savebutton = document.getElementById('savebutton');
var readonly = true;
var inputs = document.querySelectorAll('input[type="text"]');

savebutton.addEventListener('click',function(){
for (let i=0; i<inputs.length; i++) { inputs[i].toggleAttribute('readonly'); }; if (savebutton.innerHTML=="save" ) { savebutton.innerHTML="edit" ; } else { savebutton.innerHTML="save" ; } });





var inputss = document.querySelectorAll('input[type="tel"]');

savebutton.addEventListener('click',function(){
for (let i=0; i<inputss.length; i++) { inputss[i].toggleAttribute('readonly'); }; if (savebutton.innerHTML=="save" ) { savebutton.innerHTML="edit" ; } else { savebutton.innerHTML="save" ; } });


var inputsss = document.querySelectorAll('input[type="password"]');

savebutton.addEventListener('click',function(){
for (let i=0; i<inputsss.length; i++) { inputsss[i].toggleAttribute('readonly'); }; if (savebutton.innerHTML=="save" ) { savebutton.innerHTML="edit" ; } else { savebutton.innerHTML="save" ; } });