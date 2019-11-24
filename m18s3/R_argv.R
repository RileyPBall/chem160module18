args <- commandArgs(trailingOnly=T)
cat("Number or arguements:", length(args), "\n")
for (i in args) {
	cat (i, "\n")
}
