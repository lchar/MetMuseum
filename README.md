# MetMuseum
Metropolitan Museum of Art Data Science Project.

Uses the collection dataset from the Metropolitan Museum of Art.
Dataset link: https://github.com/metmuseum/openaccess

The notebook has two parts:
* The first part extracts the acquisition year from the *Credit Line* entry of each piece and creates a timeline of acquisitions for the museum as a whole or per department.
* The second part uses a small set of metadata to predict the department of a piece using a Naive Bayes Classifier.

The datasets are manipulated using the *Pandas* package, plots were created with the *matplotlib* and *plotly* packages and the classifier uses the *nltk* package.

