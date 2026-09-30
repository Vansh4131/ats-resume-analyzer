import streamlit as st
from version3 import ATSScanner

st.title("🚀 Smart ATS Resume Scanner")
st.write("Upload your Resume and paste the Job Description to see if you survive the robots.")

jd_input = st.text_area("Paste Job Description:")
uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if st.button("Scan Resume") and uploaded_file and jd_input:
    scanner = ATSScanner()

    resume_text = scanner.extract_text_from_resume(uploaded_file)

    # Run Analysis
    set_score, matches, missing = scanner.scan(resume_text, jd_input)
    cosine_score = scanner.calculate_cosine_similarity(resume_text, jd_input)
    gap_report = scanner.skills_gap_analysis(set(missing))

    # Scores
    col1, col2 = st.columns(2)
    col1.metric("Keyword Match", f"{set_score:.1f}%")
    col2.metric("AI Match", f"{cosine_score:.1f}%")

    # Verdict
    st.divider()
    if cosine_score < 50:
        st.error("Verdict: AUTO-REJECTED. Resume doesn't match this JD.")
    elif cosine_score < 80:
        st.warning("Verdict: MAYBE. Needs improvement.")
    else:
        st.success("Verdict: INTERVIEW LIKELY. Great match!")

    # Skills Gap Report
    st.divider()
    st.subheader("📊 Skills Gap Analysis")
    if gap_report:
        for category, words in gap_report.items():
            st.markdown(f"**{category}:** {', '.join(sorted(words))}")
    else:
        st.success("No significant skill gaps found!")

    # Matched keywords
    st.divider()
    st.subheader("✅ Matched Keywords")
    if matches:
        st.write(", ".join(sorted(matches)))
    else:
        st.write("No matches found.")