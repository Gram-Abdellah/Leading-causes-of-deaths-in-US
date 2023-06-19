-- noinspection SqlResolveForFile @ column/"Accidents (unintentional injuries) (V01-X59,Y85-Y86)"

-- noinspection SqlResolveForFile @ column/"Accidents (unintentional injuries) (V01-X59,Y85-Y86)"

-- I) cleaning the data
-- 1) join tables : inner join

select  * from deaths as d
inner join causes c on c.id = d.cause
inner join state s on s.id = d.state ;

-- 2) clean data :
-- cast deaths number from Text to Integer

select  Year , s.state , c.cause , CAST(d.Deaths AS int) from deaths as d
inner join causes c on c.id = d.cause
inner join state s on s.id = d.state ;

update deaths
set Deaths = CAST(Deaths AS int) ;


-- remove extra spaces from cause name :

select  Year , Trim(c.cause) , d.Deaths from deaths as d
inner join causes c on c.id = d.cause ;

update causes
set cause = Trim(cause) ;

-- transform the death cause with conditional expression :
select sum(Deaths)  as   count_deaths,
case
           when c.cause== "Accidents '(unintentional injuries) (V01-X59,Y85-Y86)" THEN  'Accidents'
           when c.cause== "Alzheimer's disease (G30)"   THEN  "Alzheimer's disease"
           when c.cause== "Cerebrovascular diseases (I60-I69)"   THEN  'Cerebrovascular diseases'
           when c.cause== "Chronic lower respiratory diseases (J40-J47)"   THEN  'Chronic lower respiratory diseases'
           when c.cause== "Diabetes mellitus (E10-E14)"   THEN  'Diabetes mellitust'
           when c.cause== "Diseases of heart (I00-I09,I11,I13,I20-I51)"   THEN  'Diseases of heart'
           when c.cause== "Influenza and pneumonia (J09-J18)"  THEN  'Influenza and pneumonia'
           when c.cause== "Intentional self-harm (suicide) (*U03,X60-X84,Y87.0)" THEN  'Intentional self-harm'
           when c.cause== "Malignant neoplasms (C00-C97)"    THEN  'Malignant neoplasms'
           when c.cause== "Nephritis, nephrotic syndrome and nephrosis (N00-N07,N17-N19,N25-N27)"  and 29  THEN  'Nephritis, nephrotic syndrome and nephrosis'
           ELSE 'other'
END AS Cause
from deaths as d
inner join causes c on c.id = d.cause
inner join state s on s.id = d.state
where c.id >1 and s.id <> 1
Group by c.cause
order by count_deaths desc ;


-- 2) What are the top five leading causes of deaths in each state ?

select c.cause , sum(d.deaths) as Sum_deaths from deaths as d
inner join causes c on c.id = d.cause
inner join state s on s.id = d.state
where c.id <> 1 and s.id <> 1
Group by c.cause
order by Sum_deaths DESC ;

-- 3) Age-adjusted Death Rates for All causes between 1999 to 2017 :
select year , s.state ,AIDR from deaths as d
inner join causes c on c.id = d.cause
inner join state s on s.id = d.state
where c.id == 1 and s.id == 1
group by year ,s.state
order by Year desc ;
-- 4) what is the state that have the highest Number of deaths in US?
select  s.state,sum(Deaths) as sum_deaths from deaths as d
inner join causes c on c.id = d.cause
inner join state s on s.id = d.state
where c.id <>1  and s.id <> 1
group by s.state
order by sum_deaths DESC ;
-- 5) Which states have the highest mortality rates for specific causes of death?
select c.cause ,max(Deaths),s.state , d.year from deaths as d
inner join causes c on c.id = d.cause
inner join state s on s.id = d.state
where c.id <> 1  and s.id <> 1
group by  c.cause
order by max(Deaths) desc ;

-- why in 1999 Diseases of heart is cause that have the maximum Number of death in US ? what happened in 1999?

-- 6) which year have the highest deaths for each cause ?

select  c.cause ,d.Year ,Deaths from deaths as d
inner join causes c on c.id = d.cause
inner join state s on s.id = d.state
where c.id <>1  and s.id == 1
group by c.cause
order by Deaths DESC ;

-- that's only mean that the deaths numbers are increasing over time

-- 7 ) What is the trend in the number of deaths caused by specific causes over the past decade?
select  c.cause ,s.state,d.Year ,d.Deaths from deaths as d
inner join causes c on c.id = d.cause
inner join state s on s.id = d.state
where c.id <>1  and s.id <> 1
group by c.cause ,s.state
order by c.cause , d.Deaths DESC ;


--8)What is the proportion of deaths caused by preventable causes ?
select  c.cause , (select  max(dt.Deaths) , d.Year  from deaths dt
                  inner join state st on st.id = dt.state
                  inner join causes ct on ct.id = dt.cause where  st.id <> 1
                  and ct.cause == "Accidents (unintentional injuries) (V01-X59,Y85-Y86)") as Max_deaths
    from deaths as d
inner join causes c on c.id = d.cause
inner join state s on s.id = d.state
where c.id <>1  and s.id <> 1 and c.cause == "Accidents (unintentional injuries) (V01-X59,Y85-Y86)"
group by c.cause
order by c.cause , d.Deaths DESC ;

--9)Which leading cause of death has shown the most significant change over time?
select c.cause ,Year ,sum(d.Deaths) from deaths as d
inner join causes c on c.id = d.cause
inner join state s on s.id = d.state
where c.id <>1  and s.id <> 1
group by  c.cause ,Year ;

--Diseases of heart from  : from 1999 to 2017 The number of deaths is stable
--Influenza and pneumonia : from 1999 to 2017 The number of deaths is declining

--10)Can we identify any clusters or patterns in the leading causes of death across different states?
select c.cause  ,max(d.Deaths) as MAx_deaths , s.state from deaths as d
inner join causes c on c.id = d.cause
inner join state s on s.id = d.state
where c.id <>1  and s.id <> 1 and d.state <> 6
group by  c.cause ;

-- Question output :
--1) why in 1999 Diseases of heart is cause that have the maximum Number of death in US ? what happened in 1999?
--2) why Diseases of heart the cause that have highest number od deaths  ?
--3) why California have the highest number of deaths in each cause ?

