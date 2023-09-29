namespace Hypnos.Data
{
    public class HypnosQuestion
    {
        public int Qno { get; set; }
        public string? Category { get; set; }
        public string? Title { get; set; }
        public string? Question { get; set; }
        public List<string>? Choices { get; set; }
        public int AnswerIndex { get; set; }
        public int Score { get; set; }

        public HypnosQuestion()
        {
            Choices = new List<string>();
        }
    }
}
