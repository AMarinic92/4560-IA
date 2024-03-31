const InfoModal = () => {
    return (
        <dialog id="info_modal" className="modal">
            <div className="modal-box prose-lg glass">
                <h3 className="font-bold text-lg">What is this Extension?</h3>
                <p className="py-4 ">
                    Our AI-powered Accessibility Checker is aimed at streamlining the process of
                    ensuring digital content is accessible to all users. Leveraging advanced machine
                    learning algorithms, our platform efficiently scans websites to detect potential
                    accessibility issues. Our Accessibility Checker offers thorough analysis and
                    practical recommendations for improvement. By providing developers, designers,
                    and content creators with valuable insights, our solution contributes to creating
                    a more inclusive digital environment where everyone can access and engage with
                    content effortlessly.</p>
            </div>
            <form method="dialog" className="modal-backdrop">
                <button>close</button>
            </form>
        </dialog>
    );
}

export default InfoModal;