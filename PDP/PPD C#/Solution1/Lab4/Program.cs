using System;
using Lab4.Parser;
using System.Collections.Generic;

namespace  Lab4;

class Program
{
    private static readonly List<string> Urls = new()
    {
        "www.reqbin.com/echo",
        "www.dspcluj.ro/HTML/CORONAVIRUS/incidenta.html"
            
    };

    static void Main()
    {
        //new Callback(Urls);
                
            
        new TaskSolution(Urls);
            
        //new AsyncAwaitSolution(Urls);
           
          
        
    }
}