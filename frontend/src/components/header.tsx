import { useState } from "react";
import { getUrl } from "../utils/chrome";
import { ChangeIsReady, ResetState } from "../interfaces/functions";
import { checker } from "../utils/checker"


const Header = ({ changeIsReady, resetState }: { changeIsReady: ChangeIsReady, resetState: ResetState }) => {
    const [init, setInit] = useState<boolean>(false)
    const [website, setWebsite] = useState<string | null>(null)


    return (
        <div className="flex flex-col justify-start px-5 pt-5">
            <h1 className="mb-3 text-xl font-bold">Accessability Checker</h1>
            <div className="mb-3">
                <a
                    className="link link-primary text-lg mb-3"
                    onClick={
                        () => {
                            const modal = document?.getElementById('info_modal') as HTMLDialogElement;
                            modal?.showModal();
                        }
                    }
                >


                    What is this extension?
                </a>

                <div className="flex flex-row   ">
                    <p className="text-base">Checking:</p>
                    <p className="font-bold text-ellipsis text-base">{website}</p>
                </div>
            </div>
            <div className="flex flex-row flex-wrap justify-between">


                <button
                    className="btn btn-secondary "
                    onClick={
                        async () => {
                            const url = await getUrl();
                            if (url) {
                                checker(url)
                                setWebsite(url);
                                changeIsReady(true, url as string);
                                setInit(true);
                            }

                        }
                    }
                    disabled={init}
                >
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-6 h-6">
                        <path d="M8.25 10.875a2.625 2.625 0 1 1 5.25 0 2.625 2.625 0 0 1-5.25 0Z" />
                        <path fillRule="evenodd" d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25Zm-1.125 4.5a4.125 4.125 0 1 0 2.338 7.524l2.007 2.006a.75.75 0 1 0 1.06-1.06l-2.006-2.007a4.125 4.125 0 0 0-3.399-6.463Z" clipRule="evenodd" />
                    </svg>


                    Analyze website
                </button>

                <button
                    className="btn btn-accent"
                    onClick={
                        () => {
                            setInit(false);
                            setWebsite(null);
                            resetState();
                        }
                    }
                    disabled={!init}
                >
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-6 h-6">
                        <path fillRule="evenodd" d="M4.755 10.059a7.5 7.5 0 0 1 12.548-3.364l1.903 1.903h-3.183a.75.75 0 1 0 0 1.5h4.992a.75.75 0 0 0 .75-.75V4.356a.75.75 0 0 0-1.5 0v3.18l-1.9-1.9A9 9 0 0 0 3.306 9.67a.75.75 0 1 0 1.45.388Zm15.408 3.352a.75.75 0 0 0-.919.53 7.5 7.5 0 0 1-12.548 3.364l-1.902-1.903h3.183a.75.75 0 0 0 0-1.5H2.984a.75.75 0 0 0-.75.75v4.992a.75.75 0 0 0 1.5 0v-3.18l1.9 1.9a9 9 0 0 0 15.059-4.035.75.75 0 0 0-.53-.918Z" clipRule="evenodd" />
                    </svg>

                    Reset
                </button>
            </div>

        </div>
    )
}

export default Header;