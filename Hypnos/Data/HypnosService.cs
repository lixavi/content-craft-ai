using Google.Protobuf.WellKnownTypes;
using Hypnos.Pages;
using static System.Formats.Asn1.AsnWriter;
using System.Security.Cryptography;

namespace Hypnos.Data
{
    public class HypnosService
    {
        private static List<HypnosQuestion>? Quesions;


        static HypnosService()
        {
            Quesions = new List<HypnosQuestion>()
            {
                new HypnosQuestion
                {
                    Qno=1,
                    Category="sa",
                    Title="Sleep_Apnea",
                    Question = "Do you snore loudly?",
                    Choices = new List<string> {"Yes", "No","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
                   new HypnosQuestion
                {
                    Qno=2,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "Do you often feel tired, sleepy or fatigued during the daytime?",
                    Choices = new List<string> {"Yes", "No","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
                   new HypnosQuestion
                {
                    Qno=3,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "Has anyone observed you stop breating in your seelp?",
                    Choices = new List<string> {"Yes", "No","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
                  new HypnosQuestion
                {
                    Qno=4,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "Do you have (or are you being treated for) high blood pressure",
                    Choices = new List<string> {"Yes", "No","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
                      new HypnosQuestion
                {
                    Qno=5,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "Sitting and reading ",
                    Choices = new List<string> {"Never", "slight","moderate","high","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
                          new HypnosQuestion
                {
                    Qno=6,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "Sitting and watching TV",
                    Choices = new List<string> {"Never", "slight","moderate","high","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
                              new HypnosQuestion
                {
                    Qno=7,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "Sitting inactive in a public space",
                    Choices = new List<string> {"Never", "slight","moderate","high","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
                                  new HypnosQuestion
                {
                    Qno=8,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "As a passenger in a car for one hour without a break",
                    Choices = new List<string> {"Never", "slight", "moderate", "high","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
                                      new HypnosQuestion
                {
                    Qno=9,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "Lying down to rest in the afternoon ",
                    Choices = new List<string> {"Never", "slight", "moderate", "high","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
                                          new HypnosQuestion
                {
                    Qno=10,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "Sitting and talking to someone",
                    Choices = new List<string> {"Never", "slight", "moderate", "high","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                                          },
                        new HypnosQuestion
                {
                    Qno=11,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "Sitting quietfly after lunch without alcohol",
                    Choices = new List<string> {"Never", "slight", "moderate", "high","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
                 new HypnosQuestion
                {
                    Qno=12,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "In a care, while stopped for a few minutes in traffic",
                    Choices = new List<string> {"Never", "slight", "moderate", "high","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
 new HypnosQuestion
                {
                    Qno=13,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "How many times do you typically wake up during the nighttime ",
                    Choices = new List<string> {"0", "1-3",">3","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
 new HypnosQuestion
                {
                    Qno=14,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "What position do you believe you spend most of your sleep time in ",
                    Choices = new List<string> {"Back", "side","stomach","recliner","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
 new HypnosQuestion
                {
                    Qno=15,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "Do you often wake up with a dry mouth or morning headache",
                    Choices = new List<string> {"Yes", "No","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
 new HypnosQuestion
                {
                    Qno=16,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "Do you often take scheduled or unscheduled naps",
                    Choices = new List<string> {"Yes", "No","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
 new HypnosQuestion
                {
                    Qno=17,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "Have you gained weight in last 3-5 years",
                    Choices = new List<string> {"freetext"},
                    AnswerIndex = 1,
                    Score = 3
                },
  new HypnosQuestion
                {
                    Qno=18,
                    Category="sa",Title="Sleep_Apnea",
                    Question = "Is there anything else you would like to tell us about your sleep",
                    Choices = new List<string> {"freetext"},
                    AnswerIndex = 1,
                    Score = 3
                },



  /*       Legs Movement */

      new HypnosQuestion
                {
                    Qno=1,
                    Category="Le",Title="Leg",
                    Question = "Do you experience an uncomfortable urge to move your legs or feet, typically accompanied by unpleasant sensations ",
                    Choices = new List<string> {"Yes", "No","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
        new HypnosQuestion
                {
                    Qno=20,
                    Category="Le",Title="Leg",
                    Question = "Is this urge or uncomfortable feeling made worse by periods of inactivty or rest",
                    Choices = new List<string> {"Yes", "No","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
  new HypnosQuestion
                {
                    Qno=21,
                    Category="Le",Title="Leg",
                    Question = "Is this urge or sensation reliveved by walking or by moving your legs",
                    Choices = new List<string> {"Yes", "No","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
  new HypnosQuestion
                {
                    Qno=22,
                    Category="Le",Title="Leg",
                    Question = "Do these symptoms only occur, or at least mostly occur, during the evening or nighttime hours",
                    Choices = new List<string> {"Yes", "No","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
  new HypnosQuestion
                {
                    Qno=23,
                    Category="Le",Title="Leg",
                    Question = "Do you have any of the following ",
                    Choices = new List<string> { "Fibromyalgia", "chronic muscle pains", "swelling in your legs", "abnormal blood flow to your legs", "leg cramps", "chronic foot tapping", "history of anemia", "Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
  new HypnosQuestion
                {
                    Qno=24,
                    Category="Le",Title="Leg",
                    Question = "Has this occurred on at least 5 total occasions over the course of the last year ",
                    Choices = new List<string> {"Yes", "No","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
    new HypnosQuestion
                {
                    Qno=25,
                    Category="Le",Title="Leg",
                    Question = "When these symptoms occur, do they typically occur >/= 2 times per week, or <2 times per week",
                    Choices = new List<string> { ">/=2", "<2","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },

      /*       Sleepniess */

                new HypnosQuestion
                {
                    Qno=26,
                    Category="SL",Title="Sleepiness",
                    Question = "How long have you worked in your current position?",
                    Choices = new List<string> { "(0-3 months", "3-6 months", "6-12 months", "> 12 months","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
                  new HypnosQuestion
                {
                    Qno=27,
                    Category="SL",Title="Sleepiness",
                    Question = "What types of shifts do you typically work?",
                    Choices = new List<string> {"1st Shift", "2nd Shift", "Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
                    new HypnosQuestion
                {
                    Qno=28,
                    Category="SL",Title="Sleepiness",
                    Question = "How many hours of sleep do you typically get per night?",
                    Choices = new List<string> {"Yes", "No","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
                      new HypnosQuestion
                {
                    Qno=29,
                    Category="SL",Title="Sleepiness",
                    Question = "Are you often exposed to bright light leading up to bed time?",
                    Choices = new List<string> {"Yes", "No","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
                        new HypnosQuestion
                {
                    Qno=30,
                    Category="SL",Title="Sleepiness",
                    Question = "Is your sleep environement generally dark, cool and quiet?",
                    Choices = new List<string> {"<1", "1-2","2-4",">4","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },
                 new HypnosQuestion
                {
                    Qno=30,
                    Category="SL",Title="Tobacco",
                    Question = "Do you use electronics in the bedroom?",
                    Choices = new List<string> {"Yes", "No","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },

    //Tobacco 

                new HypnosQuestion
                {
                    Qno=30,
                    Category="SL",Title="Tobacco",
                    Question = "Do you currently smoke tobacco cigarettes",
                    Choices = new List<string> {"Yes", "No","Please Select"},
                    AnswerIndex = 1,
                    Score = 3
                },


                new HypnosQuestion
                {
                    Qno=31,
                    Category="SL",Title="Tobacco",
                    Question = "Is your sleep environement generally dark, cool and quiet?",
                    Choices = new List<string> {"freetext"},
                    AnswerIndex = 1,
                    Score = 3
                },

                new HypnosQuestion
                {
                    Qno=32,
                    Category="SL",Title="Tobacco",
                    Question = "What time of day do you typically smoke your first cigarette",
                    Choices = new List<string> {"freetext"},
                    AnswerIndex = 1,
                    Score = 3
                },
                       
                new HypnosQuestion
                {
                    Qno=30,
                    Category="SL",Title="Tobacco",
                    Question = "Approximately how old were you when you started smoking",
                    Choices = new List<string> {"freetext"},
                    AnswerIndex = 1,
                    Score = 3
                },

                new HypnosQuestion
                {
                     Qno=30,
                     Category="SL",Title="Tobacco",
                    Question = "Approximaly, how many years in total have you (did you) smoke",
                    Choices = new List<string> {"freetext"},
                    AnswerIndex = 1,
                    Score = 3
                },





            };


        }


        public Task<List<HypnosQuestion>?> GetQuestions()
        {

            return Task.FromResult(Quesions);
        }


    }
}
