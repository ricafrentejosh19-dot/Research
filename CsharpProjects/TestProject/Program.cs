
 bool validInput = false;


do{
Console.WriteLine("Enter an integer value between 5 and 10");
string num = Console.ReadLine();

if(num < 5)
  {
    Console.WriteLine("You entered" + num + ". Please enter a number between 5 and 10.");
  } 

  else if (num.Any(char.IsLetter))
  {
    Console.WriteLine("Sorry, you entered an invalid number, please try again");
  }

  else
  {
    Console.WriteLine("Your input value " + "(" + num + ")" + " has been accepted.");
    validInput = true;
  }


} while(d); 