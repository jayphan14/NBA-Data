#Created by Jay Phan COMP Final Project
#NBA data analysis



#Library----------
import matplotlib.pyplot as plt
import csv




#Varible--------------
x = True
namelist = []
Teamlist = []
Positionlist = [] 
Agelist = []
Minutelist = []
Players_age = []
Players_point = []
Rookie = []
hometeamscore = []
awayteamscore = []
NBAdata = []
teams = []
sorted_PPG = []
sorted_RPG = []
sorted_APG = []
sorted_PPG = []
sorted_PPG = []
sorted_FTPercent = []
sorted_ThreePPercent = []


user_choice = ""
b = ''
sort_choice = ""
Pname=''
Team = ''
Age = ''
Minute = ''
Position = ''
List_input1 = ''
List_input2 = ''
List_input3 = ''
List_input4 = ''
List_input5 = ''
#for graph:
colors = ['b'] * 200 + ['g'] * 200 + ['r'] * 62
legends = 'Players PPG > 10'
#Open File and Load Data
path = "NBAdata.csv" #name of file
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)
NBAdata = [row for row in reader]  #store data in NBA data
#open and load the second data list
path ="teams.csv" #name of file
file = open(path, newline='')
reader = csv.reader(file)
teams  = [row for row in reader] #store data in teams






#WELOME MESSAGE
print("Welcome to NBA Data Analysis by Jay Phan ")
print("Data is from NBA Stuffer, Stats are updated every 10 minutes\n")
while x ==True:
  print("MAIN MENU: ")
  user_choice = input(" Enter [1] to search the data \n Enter [2] to sort the data \n Enter [3] to graph data \n Enter [4] to see award predictions \n Enter [5] to see match prediction \n Enter [6] to quit\n ================== \n") #print big menu and get user input



#SEARCH FUNCTION----------------
  if user_choice == "1":
    print("You haved chosen to search for players")
    print("====Now please enter \n 1. To search by player's name \n 2. To search by player's teams \n 3. To search by player's position \n 4. To search by player's age\n 5. To search by player's minute per game") #Options for user to choose
  
    b = int(input("")) #get user input and store as b 
    #using if else statement to get search
    
    
    if b == 1:   
      print("You haved chosen to search by name")
      Pname = input("Enter the player name: ") #get the wanted name
      print(header[1:7])
      for i in range(len(NBAdata)):     #run through whole program and find wanted name 
        if NBAdata[i][1]  == Pname:   
          print (NBAdata[i])   #print the wanted data 
      print ('------------------')
    
    
    elif b == 2 :
      for i in range(len(teams)):  #print the team's inital
        print (teams[i][1], ":  ",teams[i][0] )
      Team = input("Enter the team intial: ")   #get the wanted team
      for i in range(len(NBAdata)): #go through the data
        if NBAdata[i][2]  == Team:  #if there a match team, add them to a list called Teamlist
          Teamlist.append(NBAdata[i])
      y= len(Teamlist)
      print("There are", y, "Players on the team \n")
      print(header[1:7])
      for i in range(len(Teamlist)) :
        print(Teamlist[i]) #print the wanted data 
      print ('------------------')
    
    
    elif b == 3 :
      print ("G :  Guard \n F :  Forward") #print the guards inital
      Position  = input("Enter what position you want to look for: ")#get user input for position 
      
      for i in range(len(NBAdata)):   #go through data list 
        if NBAdata[i][3]  == Position:   # find a match
          Positionlist.append(NBAdata[i])  #append matched items to a list
     
      print("In the NBA this season, There are", len(Positionlist), "Players in this position \n ")   #print total amount
      
      print(header[1:7])  #print header 
      
      for i in range(len(Positionlist)) :   #print out the wanted data
        print(Positionlist[i])
      
      print ('------------------')
    
    
    elif b == 4 :    
      Age  = float(input("Enter what age you want to look for: ")) #get user input for age wanted 
      agerange = Age+1   #use an age range to look for data 
      for i in range(len(NBAdata)):   # go through data
        if float(NBAdata[i][4]) >= Age and float(NBAdata[i][4])< agerange :  #if match found, append it to a list 
          Agelist.append(NBAdata[i])
      print("In the NBA this season, There are", len(Agelist), "Players in this age ")   #print amount 
      print(header[1:7])
      for i in range(len(Agelist)) :  
        print(Agelist[i])     #print data
      print ('------------------')
    
    
    else:
      Minute = int(input("Enter what minute you want to look for: ")) #get input minute, store them as a number 
      minuterange = Minute+1
      for i in range(len(NBAdata)): #go through data and find match
        if float(NBAdata[i][6]) >= Minute and float(NBAdata[i][6])< minuterange :
          Minutelist.append(NBAdata[i]) #add matched datas to a list
      print("In the NBA this season, There are", len(Minutelist), "Players play between",Minute,"and",minuterange,"minutes") #print amount 
      print(header[1:7])
      for i in range(len(Minutelist)) :
        print(Minutelist[i]) #print data 
      print ('------------------')





#SORT FUNCTION----------------  
  elif user_choice == "2":
    print("You haved chosen to sort the list ")
    
    sort_choice = input("Now please enter \n 1. To sort by point per game \n 2. To sort by rebound per game \n 3. To sort by player's assist per game \n 4. To sort by player's free throw percentage \n 5. To sort by player's 3 point percentage \n")

  
    PPG = lambda NBAdata: float(NBAdata[18])  #sort criteria col 17
    RPG= lambda NBAdata: float(NBAdata[19])#sort criteria col 18
    APG = lambda NBAdata:float(NBAdata[21]) #sort criteria col 20
    FTPercent = lambda NBAdata:float(NBAdata[11]) #sort criteria col 10
    ThreePPercent = lambda NBAdata:float(NBAdata[15]) #sort criteria col 14
    
  
    if sort_choice == "1":  
      sorted_PPG=sorted(NBAdata, key=PPG, reverse = True)# criteria for sort/ name of the sorted list 
      for i in range (230):
        print ("------Rank",i + 1,"------")
        print(sorted_PPG[i][1])     #print out condense list 
        print("Point per game: ",sorted_PPG[i][18])
        print ("-----------------")
      List_input1 = input("Enter next to see the full list : " ) #ask if user want to see full list 
      if List_input1 == "next":
        for i in range (len(sorted_PPG)):
          print(sorted_PPG[i])    #print full list
      print ('------------------')
    
    
    elif sort_choice == "2":
      sorted_RPG=sorted(NBAdata, key=RPG, reverse = True) # criteria for sort/ name of the sorted list 
      for i in range (230):
        print ("------Rank",i+1,"------")
        print(sorted_RPG[i][1]) #print out condense list 
        print("Rebound per game: ",sorted_RPG[i][19])
      print ("-----------------")
      List_input2 = input("Enter next to see the full list : " )
      if List_input2 == "next":
        for i in range (len(sorted_RPG)): 
            print(sorted_RPG[i]) #print full list 
      print ('------------------')
    
    
    elif sort_choice == "3":
      sorted_APG=sorted(NBAdata, key=APG, reverse = True)# criteria for sort/ name of the sorted list 
      for i in range (230):
        print ("------Rank",i+1,"------")
        print(sorted_APG[i][1])#print out condense list 
        print("Assist per game: ",sorted_APG[i][21])
      print ("-----------------")
      List_input3 = input("Enter next to see the full list : " )
      if List_input3 == "next":
        print("Assist per game",sorted_APG[i][21])
      for i in range (len(sorted_APG)):
        print(sorted_APG[i]) #print full list 
      print ('------------------')
    
    
    elif sort_choice == "4":
      sorted_FTPercent=sorted(NBAdata, key=FTPercent, reverse = True) # criteria for sort/ name of the sorted list 
      for i in range (230):
        print ("------Rank",i+1,"------")
        print(sorted_FTPercent[i][1]) #print out condense list 
        print("FreeThrow Percentage: ",sorted_FTPercent[i][11])
        print ("-----------------")
      List_input4 = input("Enter next to see the full list: " )
      if List_input4 == "next":
        for i in range (len(sorted_FTPercent)):
          print(sorted_FTPercent[i]) #print full list 
     
      print ('------------------')
    elif sort_choice == "5" :
      sorted_ThreePPercent=sorted(NBAdata,key=ThreePPercent, reverse = True) # criteria for sort/ name of the sorted list 
      for i in range (230):
        print ("------Rank",i+1,"------") #print out condense list 
        print(sorted_ThreePPercent[i][1])
        print("3 Point Percentage: ",sorted_ThreePPercent[i][15])
        print ("-----------------")
      List_input5 = input("Enter next to see the full list : " )
      if List_input5 == "next":
        
        for i in range (len(sorted_ThreePPercent)):
          print(sorted_ThreePPercent[i])  #print full list 
      
      print ('------------------')  




#GRAPH FUNCTION

  elif user_choice == "3": 
    PPG = lambda NBAdata: float(NBAdata[18]) #key for sort
    sorted_PPG=sorted(NBAdata, key=PPG, reverse = True) #sort data by point
    
    for i in range (len(sorted_PPG)):
      Players_age.append(float(sorted_PPG[i][4])) #get x varible
      Players_point.append(float(sorted_PPG[i][18])) #get y varibles

    plt.title ("2021 NBA Season - Players age and their points per game ")  #set the title 
    plt.xlabel("Players' Age")   #label
    plt.ylabel("Players' Point per Game") #label
    plt.scatter (Players_age, Players_point,label =legends, s = 10, c=colors)  #graph a scatter plot
  
    plt.legend(loc = 'upper left')  #include the legend 

    plt.grid(True)
    plt.savefig('plot.png') #show the graph

    print ('------------------')

#PREDICTED AWARDS
  elif user_choice == "4": 
    print("You have chosen to see predicted awards") #print message
    MVP = lambda NBAdata:float(NBAdata[18]) +float(NBAdata[19]) + float(NBAdata[21] ) #MVP sorting criteria

    MVPlist=sorted(NBAdata, key=MVP, reverse = True) #sort data 
    print ("-----Most Valuble Players Prediction:  ")
    
    for i in range (3):
      print ("Number",i+1,MVPlist[i][1])
    print("") #print out top 3 MVP candidate
    


    print ("-----Rookie of the Year prediction: ")
    for i in range(len(NBAdata)):
      if float(NBAdata[i][4]) < 20: #find all player that are younger than 20 years old
        Rookie.append(NBAdata[i])  #store it in a list called Rookie
    ROY = lambda Rookie: float(Rookie[18]) +float(Rookie[19]) + float(Rookie[21]) #sort data
    sorted_ROY = sorted(Rookie, key = ROY, reverse = True)
    for i in range (3):
      print ("Number",i+1, sorted_ROY[i][1]) # print out top 3 candidate
    print("") 
    
    
    
    
    print ('------------------')
#MATCH PREDICTION  
  elif user_choice =="5":
    
    print("You have choosen to predict score")
    for i in range(len(teams)):
      print (teams[i][1], ":  ",teams[i][0] ) #print out list of team
    print(("Please enter home team: "))
    hometeam = input("") #get input for home team
    print(("Please enter away team: "))
    awayteam = input("") #get input for away team

    for i in range(len(NBAdata)):  #run through the data
      if NBAdata[i][2] == hometeam : 
        hometeamscore.append(float(NBAdata[i][18])) #append match to a list
      if NBAdata[i][2] == awayteam :
        awayteamscore.append(float(NBAdata[i][18])) #append match to a list
      
    if sum(hometeamscore) > sum(awayteamscore): #compare sum of 2 team
      print (hometeam,"will win the game") #print who will win
      print ("Score : ", hometeam, round(sum(hometeamscore)), awayteam,round(sum(awayteamscore) ))  #print score
    else: 
      print (awayteam,"will win the game") #print who will win
      print ("Score : ", hometeam, round(sum(hometeamscore)), awayteam,round(sum(awayteamscore) ))#print score 
    
    hometeamscore.clear()  #clear list
    awayteamscore.clear()  #clear list

    print ('------------------')


#QUIT OPTION
  else: 
    break
print("You have chosen to end the program")
print ("Thank you for using the program")
  
    

    

  



