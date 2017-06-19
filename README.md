# EECS 442: final project

See [final.pdf](https://github.com/jstarkman/EECS-442/blob/master/final.pdf) for
full report.  Short version: viewing the Expedia website via a mobile browser
(or the app) does not appear to cause more or fewer bookings than viewing the
site via a desktop or laptop browser, as conditioned on:

* user_location_country == hotel_country
* is_package
* srch_co - srch_ci,
* srch_adults_cnt
* srch_children_cnt
* srch_rm_cnt
* prop_is_branded
* prop_starrating
* distance_band
* hist_price_band
* popularity_band


## Prompt

`<paraphrase>`
Conduct a causal inference study of some kind, using several methods show in
class (e.g., IP weighting, matching, ...).
`</paraphrase>`

> Not all data sets are suitable for causal inference.  You need to verify that
> (conditional) exhangeability, positivity and well-defined interventions are at
> least plausible for chosen variables in the data set.
>
> You should prepare a 6-10 page report describing the problem, data sets,
> analysis, and results in detail.  It is due the last day of classes.

## Data source

The dataset used in this report was released by Expedia in early April 2017 for
the American Statistical Association's annual Datafest event.  It consists of
two files, a two-gigabyte file and a hundred-megabyte file.
