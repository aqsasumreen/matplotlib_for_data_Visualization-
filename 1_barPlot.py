import matplotlib.pyplot as plt
x = ["python", "c++", "JS", "R"]
# to show this alphabets we need to to use jupyter notebook
y= [10,20,30,40]
plt.xlabel("language" , fontsize = 10,  )
plt.ylabel("numbers")
plt.title("survey")
c = ["y", "b", "r", "g" ]
plt.bar(x,y , width =0.4 , color = c, align = 'edge', edgecolor ='white', linewidth = 10 , linestyle = ':', alpha = 0.4, label = 'population')# align = 'edge' makes the language names appear at the edge of the bars.
# align = 'edge' makes the language names appear at the edge of the bars.
# It only has two parameters: 'center' and 'edge'.
# linewidth = 10 increases the edge width.
# alpha = 0.4 (value is between 0-1) makes the colors duller. The lower the value, the duller the colors.
# To enable the label, we use plt.legend().

plt.legend()
plt.show()





