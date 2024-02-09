const Header = () => {
    return (
        <div className="flex flex-col">
            <h1 className="mb-3 text-xl font-bold">Accessability Checker</h1>
            <div className="flex flex-row justify-between">
                <div className="">
                    <div>Score</div>
                    <div className="flex justify-center items-center glass rounded-full w-12 h-12  ">
                        <p className="font-bold">8.5</p>
                    </div>
                </div>
                <div>
                    <div className="mb-1"> Score list</div>
                
                        <p className="font-bold">Readability - 8.5</p>
                        <p className="font-bold">Alt Text - 8.5</p>

                    

                </div>

            </div>
        </div>
    )
}

export default Header;