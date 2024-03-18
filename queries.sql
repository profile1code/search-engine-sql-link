CREATE DATABASE chatbot;
USE chatbot;
CREATE TABLE queries (
id INT NOT NULL AUTO_INCREMENT,
question_column VARCHAR(500) NOT NULL,
answer_column VARCHAR(500) NOT NULL,
PRIMARY KEY (id)
 );


INSERT INTO queries (question_column, answer_column)
VALUES
('How does the program work?', 'The program is to make you the truck owner, and we pay you as a partner.'),
('How are you able to do this program?', 'We are freight brokers, we control the money as well.'),
('Is this a local position?', 'Yes it is a local position. This is 11-14 hrs, you do not need to stay overnight, and you can go home every night.'),
('How could I be a truck owner?', 'We took a 90 days qualification, it depends on your credit in 90 days, we help you to purchase.'),
('How do I qualify the truck in 90 days?', 'Each driver\'s personal situation is different, If your credit is not so good they will take 90 days in order to qualify for the truck. If your credit is good you can qualify right away through, and our company is offering a $5,000 down payment system. We will help you to qualify the truck. That is our goal and mission.'),
('Why does this work?', 'It works because we are freight brokers for a major company, and have the freight.'),
('How fast can I be a truck owner?', 'It depends on your credit, but within 90 days'),
('What is the program that helps individuals become truck owners, and how does it work?', 'N/A'),
('Can you explain how the freight brokerage company controls the money in the program that helps individuals become truck owners?', 'N/A'),
('Is the position for becoming a truck owner through the program a local position, and what are the working hours?', 'N/A'),
('How does the freight brokerage company help individuals qualify for a truck in the program, and what is their goal and mission?', 'N/A'),
('What are some reasons why the program that helps individuals become truck owners works, according to the information provided?', 'N/A'),
('How long does it take to become a truck owner through the program, and what are some factors that can affect the timeline?', 'N/A')
;

SELECT * FROM queries;

