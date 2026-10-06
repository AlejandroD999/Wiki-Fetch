
# Wiki-Fetch: Simple Terminal-based Wikipedia title search engine
Wiki-Fetch is a prototype built to understand the logic behind search engines. The main interface of this projects
lies within the command-line, making it a CLI. Upon execution, Wiki-Fetch uses the provided keyword to get matching
titles from articles data in an Sqlite database. These titles are then ranked based on a score, which is the matching proportion
between the keyword and title. In case of no existing matching titles in the database, an attempt will be made to grab new titles
and display those. 


