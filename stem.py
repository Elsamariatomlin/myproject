import matplotlib.pyplot as plt
# scores =[89,97,69,86,95,93,73]#quiz scores
# print("stem | leaf")#create a stem and leaf table 
# for  score in scores:
#     stem=score//10#tens digits
#     leaf=score%10#units digits
#     print(f"{stem}|{leaf}")

# x=range(1,len(scores)+1)#student number
# y=scores#vistual stem plot
# plt.stem(x,y,linefmt="C0-",markerfmt="o",basefmt='C3-')
# plt.title("stem plot of Quiz Scores")
# plt.xlabel("Student Number")
# plt.ylabel("Score")
# plt.show()


#histogram
# plt.hist(scores,bins=[50,60,70,80,90],color="red",edgecolor="black")#plot histogram
# plt.title("Histogram of Quiz Scores")
# plt.xlabel("Score Range")
# plt.ylabel("Number of Students")
# plt.show()



#pie chart
# fruits=["apple","orange","banana","peach"]
# counts=[10,5,8,12]
# #create pie chart
# plt.pie(counts,labels=fruits,autopct="%1.1f%%",startangle=90,colors=["red","orange","yellow",'purple'])
# plt.title("Favorite fruits")
# plt.show()




#violin plot
import seaborn as sns
import pandas as pd
# data
Data = pd.DataFrame({
    "subject": ["math"]*5 + ["science"]*5,
    "score": [80, 85, 90, 95, 100, 70, 75, 78, 82, 88]  # must match length
})

# plot
sns.violinplot(x="subject", y="score", data=Data, palette="pastel")
plt.title("Violin plot of Student Scores")
plt.show()
