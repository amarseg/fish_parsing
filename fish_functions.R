find_nascent_sites <- function(results_path, ratio_thr1, ratio_thr2)
{
  require(tidyverse)
  results <- read_csv(results_path) %>%
    group_by(cell_name, file_name) %>%
    mutate(mean_intensity = mean(INT_raw), sd_intensity = sd(INT_filt)) %>%
    mutate(ratio_intensities = INT_raw/mean_intensity) %>%
    mutate(nascent_thr1 = ifelse(ratio_intensities > ratio_thr1, TRUE, FALSE),
           nascent_thr2 = ifelse(ratio_intensities > ratio_thr2, TRUE, FALSE))
}