const LoadingCollapse = () => {
    return (
        <div tabIndex={0} className="collapse collapse-arrow border border-base-300 bg-primary mb-2">
            <input type="checkbox" />
            <div className="collapse-title text-xl font-medium">
                <div className="skeleton h-4 w-full"></div>
            </div>
            <div className="collapse-content">
                <div className="flex flex-row ">
                    <div className="flex flex-col">
                        <div className="skeleton w-32 h-32"></div>
                    </div>
                   
                    <div className="flex flex-col">
                        <div className="skeleton h-4 w-full mb-1"></div>
                        <div className="skeleton h-4 w-full mb-1"></div>
                        <div className="skeleton h-4 w-full mb-1"></div>
                    </div>

                </div>
            </div>
        </div>
    );
}

export default LoadingCollapse;