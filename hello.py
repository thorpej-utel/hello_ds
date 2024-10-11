# %%
import matplotlib.pyplot as plot
name = 'Jason'

# %%
print(f'Hello {name}')

# %%
cat = ['Mama G', 'Ziggy', 'Panda']
age = [9,7,7]

ax = plot.plot(age, label='age')
ax = plot.plot(cat, label='Name')
#plot.legend
plot.show()

# %%
