def my_love(name1,name2):
    total= (name1+name2).lower()
    count_t = total.count("t")
    count_r = total.count("r")
    count_u = total.count("u")
    count_e = total.count("e")
    score1 = count_t+count_r+count_u+count_e

    count_l = total.count("l")
    count_o = total.count("o")
    count_v = total.count("v")
    count_e = total.count("e")
    score2 = count_l+count_o+count_v+count_e
    combined_score = int(str(score1)+str(score2))
    print(f"Your love score is {combined_score}")   
my_love("Tina","Rahul")
 