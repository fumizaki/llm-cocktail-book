import { StyledCard, StyledCardBody } from "./styled-card";
import { ChatMessage } from "@/domain/schema";
import { ChatRole } from "@/domain/value";


export const ChatMessageCard = ({
    id,
    content,
    role
}: ChatMessage) => {
    return (
        <StyledCard className={`${role === ChatRole.USER ? 'bg-emerald-300' : ''}`}>
            <StyledCardBody>
                <p className="whitespace-pre-wrap break-words">{content}</p>
            </StyledCardBody>
        </StyledCard>
    )
}

