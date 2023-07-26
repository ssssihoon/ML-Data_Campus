library(dplyr)
library(data.table)
library(lubridate)
library(stringr)
library(clipr)

setwd("/Users/sihoon/Desktop/FastCampus/Section_3/CH06/HR Analytics job change of data scientists/")

df <- fread("aug_train.csv") %>% tibble()
df

df %>% 
  colnames()

df %>% head(3) %>% t

df %>% 
  group_by(gender) %>% 
  summarise(n = n())

df %>% 
  count(gender)

df_refine <- df %>% 
  mutate(id = enrollee_id %>% as.character(), # id로 명을 바꿔주고, 문자열로 형변환
         city = city %>% str_remove_all("city_") %>% as.character(), # 앞에 city_ 값을 다 빼고, 문자열로 형변환
         city_idx = city_development_index, 
         
         gender = ifelse(gender == "Male", "M", 
                  ifelse(gender == "Female", "F", 
                  ifelse(gender %>% nchar()<1, NA, gender)))) # nchar을 이용해 빈값을 NA로 처리
         rlvt_ex = ifelse(relevent_experience == "HAS relevent experience", "Y", "N"), 
         
install.packages("dlookr")

library(dlookr)
         
df %>% 
  diagnose()

install.packages("ROSE")

library(ROSE) #