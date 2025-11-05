import java.util.Random;
import java.util.Scanner;
import java.util.Timer;
class Main {
    public static void main(String[] args) {
        try{
        boolean alive=true;
        boolean validInput=true;
        Scanner scanner=new Scanner(System.in());
        Timer timer=new Timer();
     System.out.println("Hi! Apparently you fell into some random hole you can't escape. Will you progress forward? y/n");
     char ans=scanner.nextLine();
     if(ans=='y'){
         System.out.println("")
     }
        }
        catch(Exception e){
            validInput=false;
            System.out.println("I think your input is invalid. I'll reset the progress due to technical issues.")
        }
