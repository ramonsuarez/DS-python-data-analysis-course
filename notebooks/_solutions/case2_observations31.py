n_species_per_plot = survey_data.groupby(["verbatimLocality"])["name"].nunique()