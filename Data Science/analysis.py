# %%
# import our libraries
import pandas as pd
import numpy as np
import altair as alt
# %%
# import our data
dino_df = pd.read_csv('dino-data.csv')
dino_df.head()
# %%
dino_df[dino_df.isnull().any(axis=1)]
# %%
dino_df.describe(exclude=[np.number])
# %%
dino_df['period']=dino_df['period'].astype('string')
# %%
# clean our data
clean_dinos = dino_df.assign(
    geo_period = lambda x: np.where(x.period.str.contains('Triassic'),'Triassic', np.where(x.period.str.contains('Jurassic'),'Jurassic', np.where(x.period.str.contains('Cretaceous'),'Cretaceous', np.nan))),
    rel_period = lambda x: np.where(x.period.str.contains('Early'),'Early', np.where(x.period.str.contains('Mid'),'Mid', np.where(x.period.str.contains('Late'),'Late', np.nan))),
    per_split = lambda x: x.period.str.split(' ').str[2].str.split('-'),
    age_range_beg = lambda x: x.per_split.str[0],
    age_range_end = lambda x: x.per_split.str[1],
    length = lambda x: x.length.str.replace('m',''),
    named_by = lambda x: x.named_by.str.replace('and ', '').str.split(' '),
    year_named = lambda x: x.named_by.str[-1:].str[0].str.replace(')','').str.replace('(',''),
    taxonomy = lambda x: x.taxonomy.str.split(' ')
    ).filter([
    'name',
    'diet',
    'geo_period',
    'rel_period',
    'age_range_beg',
    'age_range_end',
    'lived_in',
    'type',
    'length',
    'named_by',
    'year_named',
    'taxonomy'
    ])

clean_dinos['age_range_beg']=clean_dinos['age_range_beg'].dropna().astype('int64')
clean_dinos['age_range_end']=clean_dinos['age_range_end'].dropna().astype('int64')
clean_dinos['length']=clean_dinos['length'].dropna().astype('float64')
clean_dinos.head()
# %%
clean_dinos.groupby(['geo_period']).head()
# %%
jp = ['allosaurus','ankylosaurus','apatosaurus','atrociraptor','baryonyx','brachiosaurus','carnotaurus','ceratosaurus','compsognathus','corythosaurus','dilophosaurus','dreadnoughtus','gallimimus','giganotosaurus','iguanodon','lystrosaurus','mamenchisaurus','nasutoceratops','oviraptor','pachycephalosaurus','parasaurolophus','pteranodon','pyroraptor','quetzalcoatlus','sinoceratops','spinosaurus','stegosaurus','stygimoloch','therizinosaurus','triceratops','tyrannosaurus','velociraptor']
pd.Series(jp)
movies = clean_dinos.query("name in ['allosaurus','ankylosaurus','apatosaurus','atrociraptor','baryonyx','brachiosaurus','carnotaurus','ceratosaurus','compsognathus','corythosaurus','dilophosaurus','dreadnoughtus','gallimimus','giganotosaurus','iguanodon','lystrosaurus','mamenchisaurus','nasutoceratops','oviraptor','pachycephalosaurus','parasaurolophus','pteranodon','pyroraptor','quetzalcoatlus','sinoceratops','spinosaurus','stegosaurus','stygimoloch','therizinosaurus','triceratops','tyrannosaurus','velociraptor']")
# movies = clean_dinos.assign(
#     in_jp = lambda x: np.where(x.name in ['allosaurus','ankylosaurus','apatosaurus','atrociraptor','baryonyx','brachiosaurus','carnotaurus','ceratosaurus','compsognathus','corythosaurus','dilophosaurus','dreadnoughtus','gallimimus','giganotosaurus','iguanodon','lystrosaurus','mamenchisaurus','nasutoceratops','oviraptor','pachycephalosaurus','parasaurolophus','pteranodon','pyroraptor','quetzalcoatlus','sinoceratops','spinosaurus','stegosaurus','stygimoloch','therizinosaurus','triceratops','tyrannosaurus','velociraptor'],1,0)
# )
movies.describe()
# %%
movies.sort_values(by=['age_range_beg']).head(20)
# movies.head()
# %%
jp_chart = alt.Chart(movies, title='Dinosaurs in Jurassic Park').encode(
    alt.Y('name',title='Name of Animal'),
    alt.X('geo_period', title='Time Period'),
    # color='geo_period:N',
    alt.Color('geo_period', title='Time Period')
    ).mark_circle()
jp_chart
# %%
clean_dinos['diet'].value_counts()
# %%
size_chart = alt.Chart(clean_dinos.sort_values(by=['length']), title='Length of Dinosaurs Over Time').encode(
    alt.X('age_range_beg', title='Year Lived (MYA)', sort='descending',scale=alt.Scale(zero=False)),
    alt.Y('length', title='Length of Animal in Meters'),
    alt.Color('type', title='Dinosaur Type')
).mark_circle()
size_chart
# %%
jp_chart.save('jp_chart.png')
size_chart.save('size_chart.png')
# %%
