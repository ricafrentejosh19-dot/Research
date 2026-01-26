 const score = JSON.parse(localStorage.getItem('score')) || { wins: 0, loss: 0, ties: 0 };
      displayScore();


      displayScore();
      
      

      const rockElement = document.querySelector('.rock');
      const rockEvent = () =>{ resultCompMove('rock');};

      rockElement.addEventListener('click', rockEvent);
      

      const paperElement = document.querySelector('.paper');
      const paperEvent = () =>{ resultCompMove('paper');}
      paperElement.addEventListener('click', paperEvent);

      const scissorsElement = document.querySelector('.scissors');
      const scissorsEvent = ()=> resultCompMove('scissors');

      scissorsElement.addEventListener('click', scissorsEvent);

      function pickComputerMove(){

        

         const number = Math.random();
    let compMove = '';

    if(number >=0 && number <1/3){
      compMove = 'rock';
      
    }
    else if(number >= 1/3 && number < 2/3 ){
      compMove ='paper';
    }

    else if(number >= 2/3 && number < 1){
      compMove = 'scissors';
    }

    console.log(compMove);
    return compMove;
      }

let isAutoplay = false; 
let intervalID;
const autoPlay = () =>{
        if(!isAutoplay){
        intervalID = setInterval (() =>{
          const playerMove = pickComputerMove();
          resultCompMove(playerMove);
        }, 1000);
        isAutoplay = true;
      } else{
        clearInterval(intervalID);
        isAutoplay = false;
      }

      
      }
     
    
      

          function resultCompMove(playerMove){
          const compMove = pickComputerMove();
          let result = '';

          if(playerMove === 'scissors')
          {

          if(compMove === 'rock'){
          result ='you lose';
          
        }

        else if(compMove === 'scissors'){
          result = 'tie';

          
          }
          else if(compMove === 'paper'){
            result = 'you win';
        }
       
          }
          
          else if(playerMove === 'rock'){
            
             if(compMove === 'rock'){
          result ='tie';
        }

        else if(compMove === 'scissors'){
          result = 'you win';

          
          }
          else if(compMove === 'paper'){
            result = 'you lose';
        }
       
          }

          else if(playerMove === 'paper')
          {
             if(compMove === 'rock'){
          result ='you win';
        }

        else if(compMove === 'scissors'){
          result = 'you lose';

          
          }
          else if(compMove === 'paper'){
            result = 'tie';
        }
      }

       
          

          if(result === 'you win'){
          score.wins += 1;
        }
        else if(result === 'tie'){
          score.ties +=1;
        }

        else if(result === 'you lose'){
          score.loss +=1;
        }

         
        localStorage.setItem('score', JSON.stringify(score) );
        displayScore();
        
        


      document.querySelector('.winLose').innerHTML 
      = `You 
      <img class = "moves" src = ${playerMove}-emoji.png>
       Computer: <img class = "moves" src = ${compMove}-emoji.png>
      `;

      document.querySelector('.resulta').innerHTML = `${result}`;
        


      

      }


     

      function displayScore(){
        document.querySelector('.Total-score').innerHTML = 
      `Wins: ${score.wins}, Losses: ${score.loss}, Ties: ${score.ties}`;
      }

      