import random

from django.db import models
from django.contrib.auth.models import User



QUESTIONS = [
    (1, "What are your hobbies?"),
    (2, "Do you smoke or drink?"),
    (3, "What is your kind of sleep schedule??"),
    (4, "What are your views on personal space?"),
    (5, "What are your views on homosexuality?"),
]

CHOICES = [
    [
        ("Movies and Entertainment", "Movies and Entertainment"),
        ("Sports", "Sports"),
        ("Reading Books", "Reading Books"),
        ("Listening/ Playing Music", "Listening/ Playing Music"),
        ("Hanging out with family/friends", "Hanging out with family/friends"),
    ],

    [
        ("Smoke", "Smoke"),
        ("Drink", "Drink"),
        ("Both", "Both"),
        ("None", "None"),
    ],

    [
        ("Morning Bird", "Morning Bird"),
        ("Night Owl", "Night Owl"),
        ("Somewhat Both", "Somewhat Both"),
    ],

    [
        ("What is personal space? We should know everything about each other!!!", "What is personal space? We should know everything about each other!!!"),
        ("Its the most important rule of living together", "Its the most important rule of living together"),
    ],

    [
        ("It doesn't matter to me what the gender of a person is. So I'm cool with them", "It doesn't matter to me what the gender of a person is. So I'm cool with them"),
        ("I believe that there are only two genders", "I believe that there are only two genders"),
    ],
]

def generate_questions():
    questions = QUESTIONS.copy()
    generated =  []
    for _ in range(3):
        q = random.choice(questions)
        generated.append(q)
        questions.remove(q)
    return sorted(generated)

def generate_choices(question_num):
    return CHOICES[int(question_num)-1]



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='images')
    name = models.TextField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, help_text="(F)emale, (M)ale, (O)thers")
    phone = models.TextField(max_length=10)
    address = models.TextField(max_length=300)
    social_media = models.TextField(max_length=1000, help_text="Your social media link so we can know more about you")
    education = models.TextField(max_length=500, help_text="Details of your highest education")
    current_company = models.TextField(max_length=500, help_text="Where do you work")
    current_salary = models.TextField(max_length=500, help_text="Your current salary")
    about = models.TextField(max_length=500, help_text="Write about yourself")
    
    status = models.IntegerField(default=-1, editable=False)
    question_fields = models.TextField(default=generate_questions(), editable=False)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    @property
    def questions(self):
        questions = []
        s1 = self.question_fields.strip('[()]').split('), ')[0].strip("()")
        s2 = self.question_fields.strip('[()]').split('), ')[1].strip("()")
        s3 = self.question_fields.strip('[()]').split('), ')[2].strip("()")
        questions.append(tuple(s1.strip(" ").split(", ")))
        questions.append(tuple(s2.strip(" ").split(", ")))
        questions.append(tuple(s3.strip(" ").split(", ")))
        return questions


    def choice1(self):
        choice = generate_choices(self.questions[0][0])
        return choice
        
    def choice2(self):
        choice = generate_choices(self.questions[1][0])
        return choice
        
    def choice3(self):
        choice = generate_choices(self.questions[2][0])
        return choice
    
    @classmethod
    def common_questions(cls, user1, user2):
        question1 = user1.questions
        question2 = user2.questions
        common_questions = []
        for i in question1:
            if i in question2:
                common_questions.append(i)
        return common_questions
    
    @classmethod
    def common_answers(cls, user1, user2):
        common_questions = cls.common_questions(user1, user2)
        common_answers = []
        for i in common_questions:
            option1 = Choices.objects.get(user=user1.user, question=i[1])
            option2 = Choices.objects.get(user=user2.user, question=i[1])
            if option1.option == option2.option:
                common_answers.append(option1)
        return common_answers
    
    @classmethod
    def compatibility(cls, user1, user2):
        common_questions = len(cls.common_questions(user1, user2))
        common_answers = len(cls.common_answers(user1, user2))
        compatibility = common_answers*100/common_questions
        return compatibility 


class Choices(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    option = models.TextField()
    
    def __str__(self):
        return self.user.username + self.question
    