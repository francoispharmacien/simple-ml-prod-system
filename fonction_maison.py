import pandas as pd
def extraire_première_lettre(serie):
  return pd.DataFrame(serie.str[0])
