// week3 project.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string> 
#include <algorithm>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    ofstream Myfile("Order.txt"); //creating a file to write to

    string itemname, destination; //variable string
    double orderTotal, shippingCost = 0; // variable double
    char option;//variable char

    cout << ".............................................." << endl; // program header
    cout << "Itcs 2530 - Programming Assignment for week #3" << endl;
    cout << ".............................................." << endl;


    cout << "Please enter the item name (no spaces)..........:"; //user prompt
    cin >> itemname; //user input of item name

    cout << "Is the item fragile? (y=yes/n=no)...............:"; // asking user if item is fragile with a yes or no response
    cin >> option;

    if (option == 'Y' || option == 'y')  // if statement about yes or no answer resulting in adding $2 if yes
    {
        shippingCost += 2.00;
    }
    else if (option == 'N' || option == 'n')   // nothing added if answer is no
    {
        shippingCost == shippingCost;
    }
    else
    {
        cout << "Invalide entry, exiting program"; //exiting program if anything other than y or n
        return 0;
    }
    cout << "Please enter your order total...................:"; //asking user for total  
    cin >> orderTotal; //user input

    cout << "Please enter destination.(usa/can/aus/saturn)..........:"; //asking user for destination
    cin >> destination;//user input

    transform(destination.begin(), destination.end(), destination.begin(), toupper);// convert to uppercase"thanks for the line!"    
    transform(itemname.begin(), itemname.end(), itemname.begin(), toupper);

    if (destination.compare("USA") == 0) // first if/else if file with nested else if
    {

        if (orderTotal <= 50.00)  //if order total is less than or = to $50 shipping is $6 to USA
        {
            shippingCost += 6.00;
        }
        else if (orderTotal <= 100.00)  // if order total is greater than $50 but less than or = to 100 shipping is $9 to USA
        {
            shippingCost += 9.00;
        }

        else if (orderTotal <= 150.00) // if order total is great than $100 but less than or = to $150 shipping is $12 to USA
        {
            shippingCost += 12.00;
        }

        else if (orderTotal > 150.00) //if order total is greater that $150 shipping is free to USA
        {
            shippingCost = 0.00;
        }
    }
    else if (destination.compare("CAN") == 0)  //same as above for USA but for canada
    {
        if (orderTotal <= 50.00)
        {
            shippingCost += 8.00;
        }

        else if (orderTotal <= 100.00)
        {
            shippingCost += 12.00;
        }

        else if (orderTotal <= 150.00)
        {
            shippingCost += 15.00;
        }
        else if (orderTotal > 150.00)
        {
            shippingCost = 0.00;
        }

    }
    else if (destination.compare("AUS") == 0)  //same as above for USA but for australia 
    {
        if (orderTotal <= 50.00)
        {
            shippingCost += 10.00;
        }

        else if (orderTotal <= 100.00)
        {
            shippingCost += 14.00;
        }

        else if (orderTotal <= 150.00)
        {
            shippingCost += 17.00;
        }
        else if (orderTotal > 150.00)
        {
            shippingCost = 0.00;
        }

    }
    else if (destination.compare("SATURN") == 0)  //same as above for USA but for australia 
    {
        if (orderTotal <= 50.00)
        {
            shippingCost += 10.00;
        }

        else if (orderTotal <= 100.00)
        {
            shippingCost += 14.00;
        }

        else if (orderTotal <= 150.00)
        {
            shippingCost += 17.00;
        }
        else if (orderTotal > 150.00)
        {
            shippingCost = 0.00;

        }
        else
        {
            cout << "Invalide Entry, exiting program" << endl; //exiting program if anything other than (USA,CAN,AUS)
            return 0;
        }
    }


        cout << "Your Item is......................................." << setprecision(2) << fixed << itemname << endl;//output
        cout << "Your shipping cost is .............................$" << setprecision(2) << fixed << shippingCost << endl;
        cout << "You are shipping to ..............................." << setprecision(2) << fixed << destination << endl;
        cout << "Your total shipping costs are......................$" << setprecision(2) << fixed << shippingCost + orderTotal << endl;
        cout << "---------------------------------------------------Thank You!" << endl;

        Myfile << "Your Item is......................................." << setprecision(2) << fixed << itemname << endl; // writing to Order.txt file
        Myfile << "Your shipping cost is .............................$" << setprecision(2) << fixed << shippingCost << endl;
        Myfile << "You are shipping to ..............................." << setprecision(2) << fixed << destination << endl;
        Myfile << "Your total shipping costs are......................$" << setprecision(2) << fixed << shippingCost + orderTotal << endl;
        Myfile << "---------------------------------------------------Thank You!" << endl;
        Myfile.close();

        return 0;

}
