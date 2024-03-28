const InfoModal = () => {
    return (
        <dialog id="info_modal" className="modal">
            <div className="modal-box">
                <h3 className="font-bold text-lg">What is this</h3>
                <p className="py-4">Press ESC key or click outside to close</p>
            </div>
            <form method="dialog" className="modal-backdrop">
                <button>close</button>
            </form>
        </dialog>
    );
}

export default InfoModal;