const practice1 = [];
const practice2 = ['a', 'b', 'c'];








let combine = '';
for(i = 0; i <practice2.length; i ++){
  const todo = practice2[i];
  const html = `<p>${todo}</p>`;
  combine += html;

}

document.querySelector('.js-Todo-List');








function retrieveData (){
  const textbox = document.querySelector('.input1');

  const getInput1 = textbox.value;

  practice1.push(getInput1);
  console.log(practice1)

  textbox.value = '';



}

