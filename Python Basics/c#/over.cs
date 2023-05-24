// C# program to define overloading of the binary operator
using System;
 
  class TestNumber
  {

    public int num;

    // Constructor
    public TestNumber(int n)
    {
      num = n;
    }

    public TestNumber()
    {
    }

    //Overloading + operator
    public static TestNumber operator +(TestNumber num1, TestNumber num2)
    {
      TestNumber number = new TestNumber();
      number.num = num1.num + num2.num;
      return number;
    }
  }

  class OperatorMain
  {
    public static void Main()
    {

      TestNumber num1 = new TestNumber(3);
      TestNumber num2 = new TestNumber(4);
      TestNumber number = num1 + num2;

      Console.Write("Result Test Number:\n");
      Console.WriteLine("Number = {0}", number.num);
    }
  }