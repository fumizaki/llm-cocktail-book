import { StyledCard, StyledCardBody } from "./styled-card";

export const StreamingMessageCard = ({
    message
}: { message: string }) => {
    return (
        <StyledCard className={'bg-emerald-100'}>
            <StyledCardBody>
                <p className="whitespace-pre-wrap break-words">{message}</p>
            </StyledCardBody>
        </StyledCard>
    )
}