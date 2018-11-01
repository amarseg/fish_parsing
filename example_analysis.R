source('fish_functions.R')

results <- read_csv('Results.csv') %>%
  group_by(cell_name, file_name) %>%
  mutate(mean_intensity = mean(INT_raw), sd_intensity = sd(INT_filt)) %>%
  mutate(ratio_intensities = INT_raw/mean_intensity) %>%
  mutate(nascent = ifelse(ratio_intensities > 2, TRUE, FALSE))

n_nascent <- results %>%
  group_by(cell_name, file_name) %>%
  filter(nascent==T) %>%
  count(nascent)

ggplot(results, aes(x = ratio_intensities))+
  geom_histogram()+
  facet_wrap(~cell_name*file_name)


big_data <- find_nascent_sites('probes_data/Results.csv',2.5,3)
