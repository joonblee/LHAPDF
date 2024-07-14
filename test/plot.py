import matplotlib.pyplot as plt
import numpy as np
import lhapdf

# Load PDF set
print("Print PDF sets")
pdfset_ct18 = lhapdf.getPDFSet("CT18NLO")
pdfs_ct18 = pdfset_ct18.mkPDFs()
pdf_ct18 = pdfset_ct18.mkPDF(0)

pdfset_nnpdf = lhapdf.getPDFSet("NNPDF40_nlo_as_01180")
pdfs_nnpdf = pdfset_nnpdf.mkPDFs()
pdf_nnpdf = pdfset_nnpdf.mkPDF(0)

pdfset_nnpdf31 = lhapdf.getPDFSet("NNPDF31_nlo_as_0118")
pdfs_nnpdf31 = pdfset_nnpdf31.mkPDFs()
pdf_nnpdf31 = pdfset_nnpdf31.mkPDF(0)

pdfset_msht20 = lhapdf.getPDFSet("MSHT20nlo_as118")
pdfs_msht20 = pdfset_msht20.mkPDFs()
pdf_msht20 = pdfset_msht20.mkPDF(0)

# Define the Q^2 value
Q2 = 10000 

# x values
x_values = [x * 0.01 for x in range(1, 100)]
x_values_p9 = [x * 0.01 for x in range(1, 90)]

# Initialize lists to store min and max PDF values for each x
d_values_nnpdf = []
u_values_nnpdf = []
d_values_nnpdf31 = []
u_values_nnpdf31 = []
d_values_ct18 = []
u_values_ct18 = []
d_values_msht20 = []
u_values_msht20 = []
min_d_values_nnpdf = []
min_u_values_nnpdf = []
min_d_values_nnpdf31 = []
min_u_values_nnpdf31 = []
min_d_values_ct18 = []
min_u_values_ct18 = []
min_d_values_msht20 = []
min_u_values_msht20 = []
max_d_values_nnpdf = []
max_u_values_nnpdf = []
max_d_values_nnpdf31 = []
max_u_values_nnpdf31 = []
max_d_values_ct18 = []
max_u_values_ct18 = []
max_d_values_msht20 = []
max_u_values_msht20 = []

ratio_nnpdf = []
ratio_nnpdf31 = []
ratio_ct18 = []
ratio_msht20 = []
min_ratios_nnpdf = []
max_ratios_nnpdf = []
min_ratios_nnpdf31 = []
max_ratios_nnpdf31 = []
min_ratios_msht20 = []
max_ratios_msht20 = []
min_ratios_ct18 = []
max_ratios_ct18 = []

# Calculate min and max d-quark PDF values for each x across all replicas
for x in x_values_p9:
    # Calculate d/u values for NNPDF4.0 NLO
    d_value = pdf_nnpdf.xfxQ2(1, x, Q2)
    u_value = pdf_nnpdf.xfxQ2(2, x, Q2)
    d_values_nnpdf.append(d_value)
    u_values_nnpdf.append(u_value)
    ratio_nnpdf.append(d_value/u_value)

    d_mc_nnpdf = [pdf.xfxQ2(1, x, Q2) for pdf in pdfs_nnpdf]  # d-quark values for this x across all replicas
    u_mc_nnpdf = [pdf.xfxQ2(2, x, Q2) for pdf in pdfs_nnpdf]  # u-quark values for this x across all replicas

    min_d_values_nnpdf.append(np.percentile(d_mc_nnpdf, 16, axis=0))
    max_d_values_nnpdf.append(np.percentile(d_mc_nnpdf, 84, axis=0))
    min_u_values_nnpdf.append(np.percentile(u_mc_nnpdf, 16, axis=0))
    max_u_values_nnpdf.append(np.percentile(u_mc_nnpdf, 84, axis=0))

    ratios_nnpdf = [d/u for d, u in zip(d_mc_nnpdf, u_mc_nnpdf)]
    min_ratios_nnpdf.append(np.percentile(ratios_nnpdf, 16, axis=0))
    max_ratios_nnpdf.append(np.percentile(ratios_nnpdf, 84, axis=0))

for x in x_values:
    # Calculate d/u values for NNPDF3.1 NLO
    d_value = pdf_nnpdf31.xfxQ2(1, x, Q2)
    u_value = pdf_nnpdf31.xfxQ2(2, x, Q2)
    d_values_nnpdf31.append(d_value)
    u_values_nnpdf31.append(u_value)
    ratio_nnpdf31.append(d_value/u_value)

    d_mc_nnpdf31 = [pdf.xfxQ2(1, x, Q2) for pdf in pdfs_nnpdf31]  # d-quark values for this x across all replicas
    u_mc_nnpdf31 = [pdf.xfxQ2(2, x, Q2) for pdf in pdfs_nnpdf31]  # u-quark values for this x across all replicas

    min_d_values_nnpdf31.append(np.percentile(d_mc_nnpdf31, 16, axis=0))
    max_d_values_nnpdf31.append(np.percentile(d_mc_nnpdf31, 84, axis=0))
    min_u_values_nnpdf31.append(np.percentile(u_mc_nnpdf31, 16, axis=0))
    max_u_values_nnpdf31.append(np.percentile(u_mc_nnpdf31, 84, axis=0))

    ratios_nnpdf31 = [d/u for d, u in zip(d_mc_nnpdf31, u_mc_nnpdf31)]
    min_ratios_nnpdf31.append(np.percentile(ratios_nnpdf31, 16, axis=0))
    max_ratios_nnpdf31.append(np.percentile(ratios_nnpdf31, 84, axis=0))

    # Calculate d/u values for CT18
    d_value = pdf_ct18.xfxQ2(1, x, Q2)
    u_value = pdf_ct18.xfxQ2(2, x, Q2)
    d_values_ct18.append(d_value)
    u_values_ct18.append(u_value)
    du_ratio = d_value/u_value
    ratio_ct18.append(du_ratio)

    d_eigs_ct18 = [pdf.xfxQ2(1, x, Q2) for pdf in pdfs_ct18]  # d-quark values for this x across all replicas
    u_eigs_ct18 = [pdf.xfxQ2(2, x, Q2) for pdf in pdfs_ct18]  # u-quark values for this x across all replicas

    sum_diff2 = 0
    for d_value_hessian in d_eigs_ct18:
        sum_diff2 += (d_value-d_value_hessian)**2
    min_d_values_ct18.append(d_value-np.sqrt(sum_diff2))
    max_d_values_ct18.append(d_value+np.sqrt(sum_diff2))
    sum_diff2 = 0
    for u_value_hessian in u_eigs_ct18:
        sum_diff2 += (u_value-u_value_hessian)**2
    min_u_values_ct18.append(u_value-np.sqrt(sum_diff2))
    max_u_values_ct18.append(u_value+np.sqrt(sum_diff2))

    ratios_ct18 = [d/u for d, u in zip(d_eigs_ct18, u_eigs_ct18)]
    sum_diff2 = 0
    for du_ratio_hessian in ratios_ct18:
        sum_diff2 += (du_ratio-du_ratio_hessian)**2

    min_ratios_ct18.append(du_ratio-np.sqrt(sum_diff2))
    max_ratios_ct18.append(du_ratio+np.sqrt(sum_diff2))

    # Calculate d/u values for MSHT20
    d_value = pdf_msht20.xfxQ2(1, x, Q2)
    u_value = pdf_msht20.xfxQ2(2, x, Q2)
    d_values_msht20.append(d_value)
    u_values_msht20.append(u_value)
    du_ratio = d_value/u_value
    ratio_msht20.append(du_ratio)

    d_eigs_msht20 = [pdf.xfxQ2(1, x, Q2) for pdf in pdfs_msht20]  # d-quark values for this x across all replicas
    u_eigs_msht20 = [pdf.xfxQ2(2, x, Q2) for pdf in pdfs_msht20]  # u-quark values for this x across all replicas

    sum_diff2 = 0
    for d_value_hessian in d_eigs_msht20:
        sum_diff2 += (d_value-d_value_hessian)**2
    min_d_values_msht20.append(d_value-np.sqrt(sum_diff2))
    max_d_values_msht20.append(d_value+np.sqrt(sum_diff2))
    sum_diff2 = 0
    for u_value_hessian in u_eigs_msht20:
        sum_diff2 += (u_value-u_value_hessian)**2
    min_u_values_msht20.append(u_value-np.sqrt(sum_diff2))
    max_u_values_msht20.append(u_value+np.sqrt(sum_diff2))

    ratios_msht20 = [d/u for d, u in zip(d_eigs_msht20, u_eigs_msht20)]
    sum_diff2 = 0
    for du_ratio_hessian in ratios_msht20:
        sum_diff2 += (du_ratio-du_ratio_hessian)**2

    min_ratios_msht20.append(du_ratio-np.sqrt(sum_diff2))
    max_ratios_msht20.append(du_ratio+np.sqrt(sum_diff2))


# Plot
print("Draw plots")

# ratio plot
plt.figure(figsize=(8, 6))

plt.fill_between(x_values, min_ratios_ct18, max_ratios_ct18, color='blue', alpha=0.3, lw=0.5)
plt.plot(x_values, ratio_ct18, label='CT18NLO', color='blue')
plt.fill_between(x_values, min_ratios_msht20, max_ratios_msht20, color='violet', alpha=0.3, lw=0.5)
plt.plot(x_values, ratio_msht20, label='MSTH20nlo_as118', color='violet')
plt.fill_between(x_values, min_ratios_nnpdf31, max_ratios_nnpdf31, color='green', alpha=0.3, lw=0.5)
plt.plot(x_values, ratio_nnpdf31, label='NNPDF31_nlo_as_0118', color='green')
plt.fill_between(x_values_p9, min_ratios_nnpdf, max_ratios_nnpdf, color='red', alpha=0.3, lw=0.5)
plt.plot(x_values_p9, ratio_nnpdf, label='NNPDF40_nlo_as_0118', color='red')

plt.title(f'd/u Ratio at $Q^2 = {Q2} \, \mathrm{{GeV}}^2$')
plt.xlabel('$x$')
plt.ylabel('$d/u$ ratio')
#plt.xscale('log')
plt.yscale('log')
plt.xlim(0.,1.)
#plt.ylim(0.,1.)
plt.ylim(0.01,1.)
plt.legend()
plt.grid(True, which="both", ls="--") # Add grid for better readability
plt.savefig(f'du_ratio{Q2}.png')
#plt.show()

# PDF plot
plt.figure(figsize=(8, 6))

plt.fill_between(x_values, min_d_values_ct18, max_d_values_ct18, color='blue', alpha=0.3, lw=0.5)
plt.plot(x_values, d_values_ct18, label='CT18NLO (d)', color='blue', linestyle='--')
plt.fill_between(x_values, min_u_values_ct18, max_u_values_ct18, color='blue', alpha=0.3, lw=0.5)
plt.plot(x_values, u_values_ct18, label='CT18NLO (u)', color='blue')

plt.fill_between(x_values, min_d_values_msht20, max_d_values_msht20, color='violet', alpha=0.3, lw=0.5)
plt.plot(x_values, d_values_msht20, label='MSHT20nlo_as118 (d)', color='violet', linestyle='--')
plt.fill_between(x_values, min_u_values_msht20, max_u_values_msht20, color='violet', alpha=0.3, lw=0.5)
plt.plot(x_values, u_values_msht20, label='MSHT20nlo_as118 (u)', color='violet')

plt.fill_between(x_values, min_d_values_nnpdf31, max_d_values_nnpdf31, color='green', alpha=0.3, lw=0.5)
plt.plot(x_values, d_values_nnpdf31, label='NNPDF31_nlo_as_0118 (d)', color='green', linestyle='--')
plt.fill_between(x_values, min_u_values_nnpdf31, max_u_values_nnpdf31, color='green', alpha=0.3, lw=0.5)
plt.plot(x_values, u_values_nnpdf31, label='NNPDF31_nlo_as_0118 (u)', color='green')

plt.fill_between(x_values_p9, min_d_values_nnpdf, max_d_values_nnpdf, color='red', alpha=0.3, lw=0.5)
plt.plot(x_values_p9, d_values_nnpdf, label='NNPDF40_nlo_as_0118 (d)', color='red', linestyle='--')
plt.fill_between(x_values_p9, min_u_values_nnpdf, max_u_values_nnpdf, color='red', alpha=0.3, lw=0.5)
plt.plot(x_values_p9, u_values_nnpdf, label='NNPDF40_nlo_as_0118 (u)', color='red')


plt.title(f'PDFs at $Q^2 = {Q2} \, \mathrm{{GeV}}^2$')
plt.xlabel('$x$')
plt.ylabel('$xf(x)$')
#plt.xscale('log')
plt.yscale('log')
plt.xlim(0.,1.)
#plt.ylim(0.,1.)
plt.ylim(0.00001,1.)
plt.legend()
plt.grid(True, which="both", ls="--") # Add grid for better readability
plt.savefig(f'pdf{Q2}.png')


print("++ done ++")

