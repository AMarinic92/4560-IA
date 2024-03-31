import { useEffect } from "react";
import { Problem } from "../interfaces/objects";
import Card from "./card";

const Problems = ({ problems }: { problems: Problem[] }) => {


    useEffect(
        () => {
            //setProblems([{ id: "1", type: "missing alt text", message: "image https://image.com/example.jpeg" }])
        }
        , []
    )

    return (
        <div tabIndex={0} className="collapse collapse-arrow border border-base-300 bg-primary mb-2">
            <input type="checkbox" />
            <div className="collapse-title text-xl font-medium">
                Image Alt Text Analysis
            </div>
            <div className="collapse-content">
                {
                    problems.map(
                        (problem: Problem) => {
                            return (
                                <Card
                                    key={problem.id}
                                    id={problem.id}
                                    imageUrl={problem.imageUrl}
                                    type={problem.type}
                                    message=""
                                    suggestion={problem.suggestion}
                                />
                            )
                        }
                    )
                }
            </div>
        </div>
    )
}

export default Problems;