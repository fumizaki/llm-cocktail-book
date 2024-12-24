import { StyledCard, StyledCardBody } from "./styled-card";
import { Message } from "@/domain/schema";
import { MessageRole } from "@/domain/value";


export const MessageCard = ({
    id,
    content,
    role
}: Message) => {
    return (
        <StyledCard className={`${role === MessageRole.USER ? 'bg-emerald-300' : ''}`}>
            <StyledCardBody>
                <p className="whitespace-pre-wrap break-words">{content}</p>
            </StyledCardBody>
        </StyledCard>
    )
}

